def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Christian"))

#Approximate hourly AWS prices, from our Terraform projects
prices ={"nat_gateway": 0.045, "alb": 0.0225, "t3_micro": 0.0104}

for resource, hourly in prices.items():
    daily = hourly * 24
    print(f"{resource}: ${hourly}/hr, ${daily:.2f}/day")

total_daily = sum(prices.values())*24
print(f"Total: ${total_daily:.2f}/day")

ranked = sorted(prices.items(), key=lambda kv: kv[1], reverse=True)
for resource, hourly in ranked:
    print(f"{resource}: ${hourly}/hr")

expensive = [name for name, p in prices.items() if p > 0.03]
print (expensive)
