class countries:
    def __init__(self):
        self.CoE_UK = 0.233 #kg
        self.CoG_UK = 0.1884 #kg
        self.CoE_US = 0.417 #kg
        self.CoGas = 8.887#kg
        self.weektoyear = 52#number of weeks in a year
        self.daytoweek = 7 #days in a week
    #UK section for CO2 caculation
    # Funciton to Calculate Total CO2 Produced in a Week
    def COFootprint_week_UK(self,results):
      CO_housingE = results[0]*self.CoE_UK  # CO2 Produced in a Week
      CO_housingG = results[1]*self.CoG_UK # CO2 Produced in a Week
        # Calculating travel 
      CO_travel = (results[2]*self.CoGas)*self.daytoweek  # CO2 Produced Per Gallon Gassoline in one Day*7=Week of Commuting
        # Total CO2 Production
      carbon_print = CO_travel + CO_housingG + CO_housingE
      return carbon_print
    # Calculate Total CO2 Produced in a Year
    def COFootprint_year_UK(self,results):
      CO_housingE = (results[0]*self.CoE_UK)*self.weektoyear#Co2produced in a year
      CO_housingG = (results[1]*self.CoG_UK)*self.weektoyear#Co2produced in a year
        #Calculating travel 
      CO_travel = ((results[2]*self.CoGas)*self.daytoweek)*self.weektoyear# CO2 Produced Per Gallon Gassoline in a Year
        # Total CO2 Production
      carbon_print = CO_travel + CO_housingG + CO_housingE
      return carbon_print
    #US section for CO2 caculation
    def COFootprint_week_US(self,results):
      CO_housingE = (results[0]*self.CoE_US)*self.weektoyear#Co2produced in a year
        #Calculating travel 
      CO_travel = ((results[2]*self.CoGas)*self.daytoweek)*self.weektoyear# CO2 Produced Per Gallon Gassoline in a Year
        # Total CO2 Production
      carbon_print = CO_travel + CO_housingE
      return carbon_print
    # Calculate Total CO2 Produced in a Year
    def COFootprint_year_US(self,results):
      CO_housingE = (results[0]*self.CoE_US)*self.weektoyear#Co2produced in a year
        #Calculating travel 
      CO_travel = ((results[2]*self.CoGas)*self.daytoweek)*self.weektoyear# CO2 Produced Per Gallon Gassoline in a Year
        # Total CO2 Production
      carbon_print = CO_travel + CO_housingE
      return carbon_print
