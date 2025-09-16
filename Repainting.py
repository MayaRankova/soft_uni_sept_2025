nylon_qty = int(input())
paint_qty = int(input())
thinner_qty = int(input())
work_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40


# extra materials
nylon_total = nylon_qty + 2
paint_total = paint_qty + (paint_qty * 0.10)  # 10% +

# calculate material costs
total_material_cost = ((nylon_total * nylon_price) +
                       (paint_total * paint_price) +
                       (thinner_qty * thinner_price) +
                       bags_price)

worker_cost = (total_material_cost * 0.3) * work_hours

total_cost = total_material_cost + worker_cost
print(total_cost)
