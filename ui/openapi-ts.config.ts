import { defaultPlugins } from '@hey-api/openapi-ts';

export default {
  input: 'http://0.0.0.0:8000/openapi.json',
  output: 'src/client',
  plugins: [
    ...defaultPlugins,
    '@hey-api/client-fetch',
    '@tanstack/react-query', 
  ],
};