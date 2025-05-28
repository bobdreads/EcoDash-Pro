/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js',
      './**/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["Roboto", "sans-serif"],
        poppins: ["Poppins", "serif"],
        urbanist: ["Urbanist", "sans-serif"],
        spline_sans: ["Spline Sans", "sans-serif"],
        inter: ["Inter", "sans-serif"],
      },
      colors: {
        'body-light': '#F3F3F3',
        'dark-body': '#04041d',
        'color-background': '#383F6B',
        'dark-500': '#344767',
        'dark-900': '#141727',
        'heading': '#251f47',
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require("tailgrids/plugin"),
  ],
}

