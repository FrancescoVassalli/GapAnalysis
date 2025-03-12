// @ts-nocheck
import { defineConfig } from '@rsbuild/core';
import { pluginReact } from '@rsbuild/plugin-react';
import { rspack } from '@rspack/core';
import { TanStackRouterRspack } from '@tanstack/router-plugin/rspack';

export default defineConfig({
  plugins: [pluginReact()],
  tools: {
    rspack: {
      plugins: [
        TanStackRouterRspack({
          target: 'react',
          autoCodeSplitting: true,
        }),
        new rspack.CopyRspackPlugin({
          patterns: [{ from: 'favicon.svg' }],
        }),
        new rspack.DefinePlugin({
          'process.env.API_URL': JSON.stringify(process.env.API_URL),
          'process.env.DEBUG': JSON.stringify(process.env.DEBUG),
        }),
      ],
    },
  },
  source: {
    entry: { index: './src/main.tsx' },
  },
  html: {
    template: './index.html',
    templateParameters: {
      favicon: 'favicon.svg',
      faviconVersion: '1.0',
    },
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['postcss-loader'],
        type: 'css',
      },
    ],
  },
});
