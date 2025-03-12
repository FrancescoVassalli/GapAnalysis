/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file was automatically generated by TanStack Router.
// You should NOT make any changes in this file as it will be overwritten.
// Additionally, you should also exclude this file from your linter and/or formatter to prevent it from being checked or modified.

// Import Routes

import { Route as rootRoute } from './routes/__root'
import { Route as ChatImport } from './routes/chat'
import { Route as BaitImport } from './routes/bait'
import { Route as AboutImport } from './routes/about'
import { Route as IndexImport } from './routes/index'
import { Route as ChatIndexImport } from './routes/chat.index'
import { Route as ChatNewImport } from './routes/chat.new'
import { Route as ChatChatIdImport } from './routes/chat.$chatId'

// Create/Update Routes

const ChatRoute = ChatImport.update({
  id: '/chat',
  path: '/chat',
  getParentRoute: () => rootRoute,
} as any)

const BaitRoute = BaitImport.update({
  id: '/bait',
  path: '/bait',
  getParentRoute: () => rootRoute,
} as any)

const AboutRoute = AboutImport.update({
  id: '/about',
  path: '/about',
  getParentRoute: () => rootRoute,
} as any)

const IndexRoute = IndexImport.update({
  id: '/',
  path: '/',
  getParentRoute: () => rootRoute,
} as any)

const ChatIndexRoute = ChatIndexImport.update({
  id: '/',
  path: '/',
  getParentRoute: () => ChatRoute,
} as any)

const ChatNewRoute = ChatNewImport.update({
  id: '/new',
  path: '/new',
  getParentRoute: () => ChatRoute,
} as any)

const ChatChatIdRoute = ChatChatIdImport.update({
  id: '/$chatId',
  path: '/$chatId',
  getParentRoute: () => ChatRoute,
} as any)

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/': {
      id: '/'
      path: '/'
      fullPath: '/'
      preLoaderRoute: typeof IndexImport
      parentRoute: typeof rootRoute
    }
    '/about': {
      id: '/about'
      path: '/about'
      fullPath: '/about'
      preLoaderRoute: typeof AboutImport
      parentRoute: typeof rootRoute
    }
    '/bait': {
      id: '/bait'
      path: '/bait'
      fullPath: '/bait'
      preLoaderRoute: typeof BaitImport
      parentRoute: typeof rootRoute
    }
    '/chat': {
      id: '/chat'
      path: '/chat'
      fullPath: '/chat'
      preLoaderRoute: typeof ChatImport
      parentRoute: typeof rootRoute
    }
    '/chat/$chatId': {
      id: '/chat/$chatId'
      path: '/$chatId'
      fullPath: '/chat/$chatId'
      preLoaderRoute: typeof ChatChatIdImport
      parentRoute: typeof ChatImport
    }
    '/chat/new': {
      id: '/chat/new'
      path: '/new'
      fullPath: '/chat/new'
      preLoaderRoute: typeof ChatNewImport
      parentRoute: typeof ChatImport
    }
    '/chat/': {
      id: '/chat/'
      path: '/'
      fullPath: '/chat/'
      preLoaderRoute: typeof ChatIndexImport
      parentRoute: typeof ChatImport
    }
  }
}

// Create and export the route tree

interface ChatRouteChildren {
  ChatChatIdRoute: typeof ChatChatIdRoute
  ChatNewRoute: typeof ChatNewRoute
  ChatIndexRoute: typeof ChatIndexRoute
}

const ChatRouteChildren: ChatRouteChildren = {
  ChatChatIdRoute: ChatChatIdRoute,
  ChatNewRoute: ChatNewRoute,
  ChatIndexRoute: ChatIndexRoute,
}

const ChatRouteWithChildren = ChatRoute._addFileChildren(ChatRouteChildren)

export interface FileRoutesByFullPath {
  '/': typeof IndexRoute
  '/about': typeof AboutRoute
  '/bait': typeof BaitRoute
  '/chat': typeof ChatRouteWithChildren
  '/chat/$chatId': typeof ChatChatIdRoute
  '/chat/new': typeof ChatNewRoute
  '/chat/': typeof ChatIndexRoute
}

export interface FileRoutesByTo {
  '/': typeof IndexRoute
  '/about': typeof AboutRoute
  '/bait': typeof BaitRoute
  '/chat/$chatId': typeof ChatChatIdRoute
  '/chat/new': typeof ChatNewRoute
  '/chat': typeof ChatIndexRoute
}

export interface FileRoutesById {
  __root__: typeof rootRoute
  '/': typeof IndexRoute
  '/about': typeof AboutRoute
  '/bait': typeof BaitRoute
  '/chat': typeof ChatRouteWithChildren
  '/chat/$chatId': typeof ChatChatIdRoute
  '/chat/new': typeof ChatNewRoute
  '/chat/': typeof ChatIndexRoute
}

export interface FileRouteTypes {
  fileRoutesByFullPath: FileRoutesByFullPath
  fullPaths:
    | '/'
    | '/about'
    | '/bait'
    | '/chat'
    | '/chat/$chatId'
    | '/chat/new'
    | '/chat/'
  fileRoutesByTo: FileRoutesByTo
  to: '/' | '/about' | '/bait' | '/chat/$chatId' | '/chat/new' | '/chat'
  id:
    | '__root__'
    | '/'
    | '/about'
    | '/bait'
    | '/chat'
    | '/chat/$chatId'
    | '/chat/new'
    | '/chat/'
  fileRoutesById: FileRoutesById
}

export interface RootRouteChildren {
  IndexRoute: typeof IndexRoute
  AboutRoute: typeof AboutRoute
  BaitRoute: typeof BaitRoute
  ChatRoute: typeof ChatRouteWithChildren
}

const rootRouteChildren: RootRouteChildren = {
  IndexRoute: IndexRoute,
  AboutRoute: AboutRoute,
  BaitRoute: BaitRoute,
  ChatRoute: ChatRouteWithChildren,
}

export const routeTree = rootRoute
  ._addFileChildren(rootRouteChildren)
  ._addFileTypes<FileRouteTypes>()

/* ROUTE_MANIFEST_START
{
  "routes": {
    "__root__": {
      "filePath": "__root.tsx",
      "children": [
        "/",
        "/about",
        "/bait",
        "/chat"
      ]
    },
    "/": {
      "filePath": "index.tsx"
    },
    "/about": {
      "filePath": "about.tsx"
    },
    "/bait": {
      "filePath": "bait.tsx"
    },
    "/chat": {
      "filePath": "chat.tsx",
      "children": [
        "/chat/$chatId",
        "/chat/new",
        "/chat/"
      ]
    },
    "/chat/$chatId": {
      "filePath": "chat.$chatId.tsx",
      "parent": "/chat"
    },
    "/chat/new": {
      "filePath": "chat.new.tsx",
      "parent": "/chat"
    },
    "/chat/": {
      "filePath": "chat.index.tsx",
      "parent": "/chat"
    }
  }
}
ROUTE_MANIFEST_END */
