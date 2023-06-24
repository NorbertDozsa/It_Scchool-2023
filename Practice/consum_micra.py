def car_fuel_money(km):
    """Calculates gas money"""
    pret_fuel = 7.2
    FUEL_100KM = 6.2 * pret_fuel 
    
    print("-" * 50)
    print(f"Gas money for {km} km" )
    print(f"{(km * FUEL_100KM)/100} RON" )
    print("-" * 50)
  


car_fuel_money(331)