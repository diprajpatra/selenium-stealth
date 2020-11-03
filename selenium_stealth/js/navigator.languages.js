// https://github.com/berstend/puppeteer-extra/blob/c44c8bb0224c6bba2554017bfb9d7a1d0119f92f/packages/puppeteer-extra-plugin-stealth/evasions/navigator.languages/index.js

(languages) => {
  // Overwrite the `languages` property to use a custom getter.
  Object.defineProperty(Object.getPrototypeOf(navigator), 'languages', {
    get: () => languages || ['en-US', 'en']
  })
}
