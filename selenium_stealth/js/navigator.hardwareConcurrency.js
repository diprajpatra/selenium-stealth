// https://github.com/berstend/puppeteer-extra/blob/3ea4ebca4237bb45ce402ba6a44d852e3499cb5f/packages/puppeteer-extra-plugin-stealth/evasions/navigator.hardwareConcurrency/index.js

(hardwareConcurrency) => {
    const patchNavigator = (name, value) =>
        utils.replaceProperty(Object.getPrototypeOf(navigator), name, {
            get() {
                return value
            }
        })
    patchNavigator('hardwareConcurrency', hardwareConcurrency || 4)
}
