from analyzer.main import report

print("\nSMART NUMBER ANALYZER")

while True:
    try:
        n = int(input("\nEnter a number: "))
        report(n)
        break
    except:
        print("Error")
