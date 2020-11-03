// https://github.com/berstend/puppeteer-extra/blob/c44c8bb0224c6bba2554017bfb9d7a1d0119f92f/packages/puppeteer-extra-plugin-stealth/evasions/webgl.vendor/index.js

(vendor, renderer) => {
  const getParameterProxyHandler = {
    apply: function (target, ctx, args) {
      const param = (args || [])[0]
      // UNMASKED_VENDOR_WEBGL
      if (param === 37445) {
        return vendor || 'Intel Inc.' // default in headless: Google Inc.
      }
      // UNMASKED_RENDERER_WEBGL
      if (param === 37446) {
        return renderer || 'Intel Iris OpenGL Engine' // default in headless: Google SwiftShader
      }
      return utils.cache.Reflect.apply(target, ctx, args)
    }
  }

  // There's more than one WebGL rendering context
  // https://developer.mozilla.org/en-US/docs/Web/API/WebGL2RenderingContext#Browser_compatibility
  // To find out the original values here: Object.getOwnPropertyDescriptors(WebGLRenderingContext.prototype.getParameter)
  const addProxy = (obj, propName) => {
    utils.replaceWithProxy(obj, propName, getParameterProxyHandler)
  }
  // For whatever weird reason loops don't play nice with Object.defineProperty, here's the next best thing:
  addProxy(WebGLRenderingContext.prototype, 'getParameter')
  addProxy(WebGL2RenderingContext.prototype, 'getParameter')
}