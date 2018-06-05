'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')
const defaultEnv = require('./index')

module.exports = merge(prodEnv, defaultEnv, {
  NODE_ENV: '"development"',
  BASE_API: '"https://easy-mock.com/mock/5950a2419adc231f356a6636/vue-admin"',

    dev: {

      assetsPublicPath: '/vueAdmin'
      }


})
