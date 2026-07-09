// HTTP Basic Auth gate for everything under /internal/*
// Password check only — any username works. Set INTERNAL_DOCS_PASSWORD in the
// Cloudflare Pages project env vars to override the default below.

export async function onRequest(context) {
  const { request, next, env } = context;
  const PASSWORD = env.INTERNAL_DOCS_PASSWORD || "EmberTribe!2026";

  const auth = request.headers.get("Authorization") || "";
  const [scheme, encoded] = auth.split(" ");

  if (scheme === "Basic" && encoded) {
    try {
      const decoded = atob(encoded);
      const pass = decoded.slice(decoded.indexOf(":") + 1);
      if (pass === PASSWORD) {
        return next();
      }
    } catch (e) {
      // fall through to 401
    }
  }

  return new Response("EmberTribe internal — authentication required.", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="EmberTribe Internal", charset="UTF-8"',
      "Cache-Control": "no-store",
    },
  });
}
