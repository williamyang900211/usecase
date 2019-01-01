from django.db import models

# Create your models here.

class test_bill(models.Model):
    '''测试提单'''
    bill_no = models.CharField(max_length=128)  # 提单号
    re_process = models.TextField('重现过程')  # 重现过程
    test_point = models.TextField('测试要点')  # 测试要点
    data_prepare = models.TextField('数据设计')  # 数据设计
    bug_no = models.CharField(max_length=128)  # bug号    
    remarks = models.TextField('备注')  # 备注
    def __str__(self):
        return self.bill_no+'-'+self.bug_no

class use_case(models.Model):
    '''用例类，用于存储所有的用例''' 
    test_bill = models.ForeignKey(test_bill, on_delete=models.CASCADE)   # 测试提单
    use_case_no = models.CharField(max_length=128)  # 用例编号
    class_layer_one = models.CharField(max_length=128)  # 一级分类
    class_layer_two = models.CharField(max_length=128)  # 二级分类
    class_layer_three = models.CharField(max_length=128)  # 三级分类
    use_case_input = models.TextField('输入条件')  # 输入条件
    use_case_output = models.TextField('输出结果')  # 输入结果
    tester = models.CharField(max_length=128)  # 测试人
    test_result = models.CharField(max_length=128)  # 测试执行结果    
    exec_date = models.DateField('执行日期')  # 执行日期

    def __str__(self):
        return self.use_case_no+'-'+self.test_bill.bill_no+'-'+self.tester+'-'+self.exec_date
