class Calculator:
    
    @staticmethod
    def multiply(a:int,b:int)->int:
        """Multiply Two integers

        Args:
            a (int): The First integer
            b (int): The second interger

        Returns:
            int: product of a and b 
        """
        return a*b
    
    @staticmethod
    def calculate_total(*x :float)->float:
        """Claculate sum of the given list of numbers
        
        Args:
        x (list) : List of floating numbers

        Returns:
            float: The sum of the numbers of the list in x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total:float,days:int)->float:
        """Calculate daily budget

        Args:
            total (float): Total Cost
            days (int): The number of days

        Returns:
            float: Expense for a single day
        """
        return total/days if days > 0 else 0