#https://uva.onlinejudge.org/external/115/11559.pdf
def main():
    try:  
        while(True):
            nbhw = [int(x) for x in input().split()]

            minprice = nbhw[1] + 1
            for x in range(peeps[2]):
                price_per_person = int(input())
                number_of_beds = [int(x) for x in input().split()]
                number_of_beds.sort(reverse = True)

                total_cost = price_per_person * nbhw[0]

            #     print("TOTAL_COST: {}".format(total_cost))


                if number_of_beds[0] >= peeps[0] and total_cost <= (minprice-1):
            #         if total_cost < minprice:
                    minprice = total_cost

            if minprice > nbhw[1]:
                print("stay home")
            else:
                print(minprice)
    except EOFError:
        pass

if __name__=="__main__":
    main()