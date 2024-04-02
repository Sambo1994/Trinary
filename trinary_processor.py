import random

class TrinaryUnit:
    def __init__(self):
        self.previous_data = None

    def process_data(self, data):
        if data == 0:
            return "Negative"
        elif data == 1:
            return "Positive"
        elif data == "01":
            if self.previous_data is None:
                return random.choice(["Negative", "Positive"])
            else:
                return self.previous_data
        else:
            raise ValueError("Invalid input data")

    def run(self, data_stream):
        results = []
        for data in data_stream:
            result = self.process_data(data)
            results.append(result)
            self.previous_data = result
        return results

def main():
    trinary_unit = TrinaryUnit()
    data_stream = input("Enter the data stream (separate elements by spaces): ").split()
    results = trinary_unit.run(data_stream)
    print("Results:", results)

if __name__ == "__main__":
    main()