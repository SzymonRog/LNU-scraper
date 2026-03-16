float salaryAvg(int salary[], int employeesNumber)
{
    int sum_salary = 0;
    for(int i = 0; i < employeesNumber  ;i++)
    {
        sum_salary += salary[i];
    }
    
    return (float(sum_salary) / employeesNumber);
}
