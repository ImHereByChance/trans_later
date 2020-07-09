# ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMU9UUXlOVEExTmpnc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pNMk1qQXNJbFZ1YVhGMVpVbGtJam9pTVRZM1l6YzVabVl0TmpFMk5DMDBOR1kxTFdJeU5HSXRaalk1TnpBNU5UZzNPVEJrSW4xOS5objh2c1RmZDM2cHRIQldXdnZHVVE3MFJuNXRRY09adVlsdlBwNlpBM3Rn

import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MTY3Yzc5ZmYtNjE2NC00NGY1LWIyNGItZjY5NzA5NTg3OTBkOmYzODc1YWU4MTc2YTQ5MjU4YmE2ZDhjNTM5NzQ5MTRm'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
	token = auth.text

	while True:
		word = input('Перевести:')
		if word:
			headers_translate = {
			'Authorization': 'Bearer ' + token,
			}
			params = {
					'text': word,
					'srcLang': 1033,
					'dstLang': 1049
			}
			req = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
			res = req.json()
			try:
				print(res['Translation'] ['Translation'])
			except:
				print('НЕ НАЙДЕНО :(')

else:
	print('ERROR')



#usless comment
