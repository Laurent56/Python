I recently created a presentation on Getting Started with Data Quality Outlier Detection for my company Collibra. During the writing I was trying to explain about how the Interquartile Range ("IQR") formula is being used to detect outliers in a set of numbers, in this case a column in the New York Stock Exchange (NYSE) dataset.
As I wrote more about this IQR formula and how it is applied using Collibra Data Quality I realized I didn't totally understand the meaning of especially the IQR Q1 and Q3 variables, since our DQ software allows you to set this using sliders in the DQ wep app.
In order to understand all of IQR better, I decided to write an entire DQ Outlier Check with IQR from scratch using Python. To aid me in this, I watched a video "How to Find the Interquartile Range...".
I decided that for each step of the video I would perform the same steps in Python code until I had coded the entire video and gotten the same results. 
This Python file is that.
