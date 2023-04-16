input_data = 375830

weeks = input_data // 604800

days = (input_data % 604800) // 86400
# Also we can use:
# days = (input_data - weeks * 604800) // 86400,
# but it has more iterations

hours = (input_data % 86400) // 3600
# Also we can use:
# hours = (input_data - weeks * 604800 - days * 86400) // 3600,
# but it has more iterations

# minutes = (input_data % 86400) // 60
# or
minutes = (input_data % 3600) // 60
# Also we can use:
# minutes = (input_data - weeks * 604800 - days * 86400) // 60,
# or
# minutes = (input_data - weeks * 604800 - days * 86400 - hours * 3600) // 60,
# but they have more iterations

seconds = input_data % 60

print(input_data, "seconds are:",
      weeks, "week(-s),",
      days, "day(-s),",
      hours, "hours,",
      minutes, "minute(-s),",
      seconds, "second(-s).", sep=' '
      )

# result = weeks * 604800 + days * 86400 + minutes * 60 + seconds
# or
result = weeks * 604800 + days * 86400 + hours * 3600 + minutes * 60 + seconds

assert result == input_data
