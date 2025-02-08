/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./templates/**/*.html'
	],
	theme: {
		extend: {
			colors: {
				'accent': {
					100: '#92C7CF',
					200: '#b0d7d9'
				},
				'primary': '#FBF9F1',
				'secondary': '#E5E1DA',
				'dark': '#2D2D2D',
			}
		},
	},
	plugins: [],
}
