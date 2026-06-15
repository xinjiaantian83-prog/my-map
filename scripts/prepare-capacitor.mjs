import { cp, mkdir, readdir, rm } from "node:fs/promises";
import { dirname, extname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const outDir = join(root, "www");

const skipDirs = new Set([
  ".git",
  ".github",
  "android",
  "ios",
  "node_modules",
  "scripts",
  "www"
]);

const copyRootExtensions = new Set([
  ".css",
  ".gif",
  ".html",
  ".jpg",
  ".jpeg",
  ".js",
  ".json",
  ".mp3",
  ".png",
  ".svg",
  ".wav",
  ".webmanifest"
]);

await rm(outDir, { recursive: true, force: true });
await mkdir(outDir, { recursive: true });

const entries = await readdir(root, { withFileTypes: true });

for (const entry of entries) {
  if (entry.name.startsWith(".DS_Store")) continue;
  const src = join(root, entry.name);
  const dest = join(outDir, entry.name);

  if (entry.isDirectory()) {
    if (skipDirs.has(entry.name)) continue;
    await cp(src, dest, { recursive: true });
    continue;
  }

  if (entry.isFile() && copyRootExtensions.has(extname(entry.name).toLowerCase())) {
    await cp(src, dest);
  }
}

console.log("Prepared Capacitor web assets in www/");
