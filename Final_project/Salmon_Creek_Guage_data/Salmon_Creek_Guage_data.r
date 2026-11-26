library(tidyverse)
library(dplyr)

guage_2015_series <- read.csv(
"Final_project\\Salmon_Creek_Guage_data\\primary-time-series_2015.csv")

guage_2017_series <- read.csv(
"Final_project\\Salmon_Creek_Guage_data\\primary-time-series_2017.csv")

guage_2019_series <- read.csv(
"Final_project\\Salmon_Creek_Guage_data\\primary-time-series_2019.csv")

guage_2021_series <- read.csv(
"Final_project\\Salmon_Creek_Guage_data\\primary-time-series_2021.csv")

guage_2024_series <- read.csv(
"Final_project\\Salmon_Creek_Guage_data\\primary-time-series_2024.csv")

tot_stream_height_2015 <- sum(guage_2015_series["value"])

avg_stream_height_2015 <- tot_stream_height_2015/length(guage_2015_series[["value"]])
tot_stream_height_2017 <- sum(guage_2017_series["value"])
avg_stream_height_2017 <- tot_stream_height_2017/length(guage_2017_series[["value"]])
tot_stream_height_2019 <- sum(guage_2019_series["value"])
avg_stream_height_2019 <- tot_stream_height_2019/length(guage_2019_series[["value"]])
tot_stream_height_2021 <- sum(guage_2021_series["value"])
avg_stream_height_2021 <- tot_stream_height_2021/length(guage_2021_series[["value"]])
tot_stream_height_2024 <- sum(guage_2024_series["value"])
avg_stream_height_2024 <- tot_stream_height_2024/length(guage_2024_series[["value"]])


print("2015 Tot. Stream height:")
print(tot_stream_height_2015)
print('')
print("2015 Ave. Stream height:")
print(avg_stream_height_2015)
print('')
print("2017 Tot. Stream height:")
print(tot_stream_height_2017)
print("2017 Ave. Stream height:")
print(avg_stream_height_2017)
print("2019 Tot. Stream height:")
print(tot_stream_height_2019)
print("2019 Ave. Stream height:")
print(avg_stream_height_2019)
print("2021 Tot. Stream height:")
print(tot_stream_height_2021)
print("2021 Ave. Stream height:")
print(avg_stream_height_2021)
print("2024 Tot. Stream height:")
print(tot_stream_height_2024)
print("2024 Ave. Stream height:")
print(avg_stream_height_2024)