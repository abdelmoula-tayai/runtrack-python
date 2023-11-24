def draw_diagonal_carpet(n):
    bord = "+" + "-" * n + "+"
    print(bord)
    for k in range(n):
        traverse = "#" * (n - k - 1) + " " + "#" * k
        print(f"|{traverse}|")
    print(bord)

draw_diagonal_carpet(10)





