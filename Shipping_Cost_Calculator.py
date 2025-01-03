# Shipping Cost Calculator

## Input package whight and shipping rate
weight = float(input("Enter the package wight in kilograms:"))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
