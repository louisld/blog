import path from "node:path";

import { defineConfig } from "vite";

import autoprefixer from "autoprefixer";

export default defineConfig({
    root: path.join(__dirname, "./app/assets"),
    base: "/assets/",
    build: {
        outDir: path.join(__dirname, "./build/assets/"),
        manifest: "manifest.json",
        assetsDir: "bundled",
        rollupOptions: {
            input: [
                "app/assets/ts/main.ts",
                "app/assets/scss/main.scss",
                "app/assets/scss/base.scss"
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
