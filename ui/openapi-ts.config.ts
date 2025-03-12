import { defaultPlugins } from '@hey-api/openapi-ts';

export default {
  input: 'http://0.0.0.0:8000/openapi.json',
  output: 'src/client',
  plugins: [
    ...defaultPlugins,
    '@hey-api/client-fetch',
    '@hey-api/schemas',
    {
      dates: true,
      name: '@hey-api/transformers',
    },
    {
      enums: 'javascript',
      name: '@hey-api/typescript',
    },
    {
      name: '@hey-api/sdk',
      transformer: true,
    },
    '@tanstack/react-query',
  ],
};
