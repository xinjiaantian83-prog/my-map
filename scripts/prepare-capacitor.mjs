import { cp, mkdir, readFile, readdir, rm, writeFile } from "node:fs/promises";
import { dirname, extname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const outDir = join(root, "www");
const platform = process.env.CAP_PLATFORM || "web";

const skipDirs = new Set([
  ".git",
  ".github",
  "android",
  "ios",
  "node_modules",
  "scripts",
  "store-screenshots",
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

const skipRootFiles = new Set([
  "app-store-icon-1024.png",
  "apple-touch-icon 2.png",
  "apple-touch-icon.png",
  "capacitor.config.json",
  "index_backup.html",
  "index_before_gold.html",
  "launcher.html",
  "package-lock.json",
  "package.json"
]);

const appStoreBadge =
  '<a href="https://apps.apple.com/jp/app/%E7%8F%BE%E5%A0%B4%E9%9B%BB%E5%8D%93/id6776547872" onclick="openExternal(this.href);return false;" aria-label="現場電卓をApp Storeで開く"><img src="assets/store-badges/app-store-badge.svg" alt="Download on the App Store"></a>';
const googleStoreBadge =
  '<a href="https://play.google.com/store/apps/details?id=com.genbatoolbox.genbacalcnew" onclick="openExternal(this.href);return false;" aria-label="現場電卓をGoogle Playで開く"><img src="assets/store-badges/google-play-badge.png" alt="Google Play で手に入れよう"></a>';
const wanwanAppStoreUrl =
  "https://apps.apple.com/app/%E3%82%8F%E3%82%93%E3%82%8F%E3%82%93%E3%82%B3%E3%82%A4%E3%83%B3/id6780428018";
const wanwanGooglePlayUrl = "https://play.google.com/store/apps/details?id=jp.wanwancoin.app";
const wanwanAppStoreBadge =
  `<a href="${wanwanAppStoreUrl}" onclick="openExternal(this.href);return false;" aria-label="わんわんコインをApp Storeで開く"><img src="assets/store-badges/app-store-badge.svg" alt="Download on the App Store"></a>`;
const wanwanGooglePlayBadge =
  `<a href="${wanwanGooglePlayUrl}" onclick="openExternal(this.href);return false;" aria-label="わんわんコインをGoogle Playで開く"><img src="assets/store-badges/google-play-badge.png" alt="Google Play で手に入れよう"></a>`;

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

  if (entry.isFile() && copyRootExtensions.has(extname(entry.name).toLowerCase()) && !skipRootFiles.has(entry.name)) {
    await cp(src, dest);
  }
}

const indexPath = join(outDir, "index.html");
let indexHtml = await readFile(indexPath, "utf8");
let storeBadgeHtml = "";

if (platform === "ios") {
  storeBadgeHtml = appStoreBadge;
  indexHtml = indexHtml
    .replace(/var WANWAN_GOOGLE_PLAY_URL = ".*?";/, 'var WANWAN_GOOGLE_PLAY_URL = "";')
    .replace(/function buildWanwanAppBadges\(\)\{[\s\S]*?\n\}/, `function buildWanwanAppBadges(){ return ${JSON.stringify(wanwanAppStoreBadge)}; }`);
  await rm(join(outDir, "assets", "store-badges", "google-play-badge.png"), { force: true });
} else if (platform === "android") {
  storeBadgeHtml = googleStoreBadge;
  indexHtml = indexHtml
    .replace(/var WANWAN_APP_STORE_URL = ".*?";/, 'var WANWAN_APP_STORE_URL = "";')
    .replace(/function buildWanwanAppBadges\(\)\{[\s\S]*?\n\}/, `function buildWanwanAppBadges(){ return ${JSON.stringify(wanwanGooglePlayBadge)}; }`);
  await rm(join(outDir, "assets", "store-badges", "app-store-badge.svg"), { force: true });
}

indexHtml = indexHtml.replace("__FIELD_CALC_STORE_BADGES__", JSON.stringify(storeBadgeHtml));
await writeFile(indexPath, indexHtml);

console.log(`Prepared Capacitor web assets in www/ for ${platform}`);
