# 中国农历时间转成天干地支记时

import calendar
from datetime import datetime

def complete_sexagenary(year, month, day, hour):
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    def year_sexagenary(year):
        year_offset = (year - 4) % 60
        return heavenly_stems[year_offset % 10] + earthly_branches[year_offset % 12]
    
    def month_stem(year, month):
        year_stem_index = (year - 4) % 10
        month_stem_index = (year_stem_index * 2 + month) % 10
        return heavenly_stems[month_stem_index]
    
    def month_branch(year, month):
        first_day_wday, month_days = calendar.monthrange(year, month)
        first_month_branch = 2  # 寅
        if calendar.isleap(year):
            first_month_branch -= 1
        month_branch = (first_month_branch + month - 1) % 12
        return earthly_branches[month_branch]
    
    def day_sexagenary(year, month, day):
        base_date = datetime(1900, 1, 1)
        target_date = datetime(year, month, day)
        days_passed = (target_date - base_date).days
        day_offset = days_passed % 60
        return heavenly_stems[day_offset % 10] + earthly_branches[day_offset % 12]
    
    def hour_stem(year, month, day, hour):
        base_date = datetime(1900, 1, 1)
        target_date = datetime(year, month, day)
        days_passed = (target_date - base_date).days
        day_stem_index = days_passed % 10
        hour_stem_index = (day_stem_index * 2 + hour // 2) % 10
        return heavenly_stems[hour_stem_index]
    
    def hour_branch(hour):
        hour = (hour + 1) % 24
        return earthly_branches[hour // 2]
    
    year_sexagenary_result = year_sexagenary(year)
    month_stem_result = month_stem(year, month)
    month_branch_result = month_branch(year, month)
    day_sexagenary_result = day_sexagenary(year, month, day)
    hour_stem_result = hour_stem(year, month, day, hour)
    hour_branch_result = hour_branch(hour)
    
    return year_sexagenary_result, month_stem_result + month_branch_result, day_sexagenary_result, hour_stem_result + hour_branch_result

if __name__ == "__main__":
    complete_sexagenary(1990, 1, 1, 0)

