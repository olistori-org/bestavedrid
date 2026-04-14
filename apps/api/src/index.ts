import Fastify from "fastify";

const app = Fastify({ logger: true });

app.get("/health", async () => ({ status: "ok", service: "api" }));

const port = Number(process.env.PORT ?? 3000);

async function start(): Promise<void> {
  await app.listen({ port, host: "0.0.0.0" });
}

if (process.env.NODE_ENV !== "test") {
  start().catch((error) => {
    app.log.error(error);
    process.exit(1);
  });
}

export { app };
