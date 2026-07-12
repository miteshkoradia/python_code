from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    node_id: str
    mem_capacity: int
    cpu_capacity: int
    mem_available: int
    cpu_available: int


class JobScheduler:

    def __init__(self):
        self.nodes = {}
        # job_id -> (node_id, mem_required, cpu_required), so complete_job
        # knows exactly how much to give back.
        self.job_allocations = {}

    def add_node(self, node_id: str, mem_capacity: int, cpu_capacity: int) -> None:
        self.nodes[node_id] = Node(node_id, mem_capacity, cpu_capacity, mem_capacity, cpu_capacity)

    def submit_job(self, job_id: str, mem_required: int, cpu_required: int) -> str | None:
        best_node = None
        best_score = None

        for node in self.nodes.values():
            if node.mem_available < mem_required or node.cpu_available < cpu_required:
                continue

            # Best-fit for vector bin packing: score how "tight" the fit is by
            # looking at the leftover capacity *after* placing the job, as a
            # fraction of total capacity on each dimension. Squaring and
            # summing (an L2 norm) penalizes leaving one dimension nearly
            # empty while the other is packed tight -- i.e. it favors nodes
            # that end up balanced across mem/cpu, not just tight on one axis.
            mem_leftover_frac = (node.mem_available - mem_required) / node.mem_capacity
            cpu_leftover_frac = (node.cpu_available - cpu_required) / node.cpu_capacity
            score = mem_leftover_frac ** 2 + cpu_leftover_frac ** 2

            if (best_score is None or score < best_score or 
               (score == best_score and node.node_id < best_node.node_id)):
                best_score = score
                best_node = node

        if best_node is None:
            return None

        best_node.mem_available -= mem_required
        best_node.cpu_available -= cpu_required
        self.job_allocations[job_id] = (best_node.node_id, mem_required, cpu_required)
        return best_node.node_id

    def complete_job(self, job_id: str) -> None:
        if job_id not in self.job_allocations:
            return

        node_id, mem_required, cpu_required = self.job_allocations.pop(job_id)
        node = self.nodes[node_id]
        node.mem_available += mem_required
        node.cpu_available += cpu_required

    def node_status(self, node_id: str) -> tuple[int, int, int, int]:
        node = self.nodes[node_id]
        return (node.mem_available, node.mem_capacity, node.cpu_available, node.cpu_capacity)


def main():
    ops = [
        "JobScheduler",
        "add_node", "add_node",
        "submit_job", "submit_job", "submit_job",
        "node_status",
        "complete_job",
        "submit_job",
        "node_status",
    ]
    args = [
        [],
        ["n1", 16, 8],   # 16GB mem, 8 vCPU
        ["n2", 8, 16],   # 8GB mem, 16 vCPU
        ["j1", 10, 2],
        ["j2", 4, 12],
        ["j3", 4, 4],
        ["n1"],
        ["j1"],
        ["j4", 8, 2],
        ["n1"],
    ]

    results = [None]
    scheduler = JobScheduler()

    for op, arg in zip(ops[1:], args[1:]):
        method = getattr(scheduler, op)
        results.append(method(*arg))

    print(results)


if __name__ == "__main__":
    main()
