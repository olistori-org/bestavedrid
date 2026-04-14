export type WorkerHealth = {
  service: "worker";
  status: "ok";
};

export function getWorkerHealth(): WorkerHealth {
  return { service: "worker", status: "ok" };
}
