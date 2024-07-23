import path from "node:path";

import { defineConfig } from "vite";

import autoprefixer from "autoprefixer";

export default defineConfig({
    root: path.join(__dirname, "./src/assets"),
    base: "/assets/",
    build: {
        outDir: path.join(__dirname, "./build/assets/"),
        manifest: "manifest.json",
        assetsDir: "bundled",
        rollupOptions: {
            input: [
                "src/assets/ts/main.ts",
                "src/assets/scss/main.scss",
                "src/assets/scss/base.scss"
            ]
        },
        emptyOutDir: true,
        copyPublicDir: false
    },
    css: {
        postcss: {
            plugins: [
                autoprefixer({})
            ]
        }
    }
});
