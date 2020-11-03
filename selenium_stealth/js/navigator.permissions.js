// https://github.com/berstend/puppeteer-extra/blob/c44c8bb0224c6bba2554017bfb9d7a1d0119f92f/packages/puppeteer-extra-plugin-stealth/evasions/navigator.permissions/index.js

() => {
  const handler = {
    apply: function (target, ctx, args) {
      const param = (args || [])[0]

      if (param && param.name && param.name === 'notifications') {
        const result = { state: Notification.permission }
        Object.setPrototypeOf(result, PermissionStatus.prototype)
        return Promise.resolve(result)
      }

      return utils.cache.Reflect.apply(...arguments)
    }
  }

  utils.replaceWithProxy(
    window.navigator.permissions.__proto__, // eslint-disable-line no-proto
    'query',
    handler
  )
}