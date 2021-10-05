from aggregate_services import object_mapping_to_time, object_report_to_lists
import matplotlib.pyplot as plt

mapping_report_30k_blocks_stress_thread = {
    4: "reports-30k-blocks/Arangodb-4threads-summary.json",
    8: "reports-30k-blocks/Arangodb-8threads-summary.json",
    16: "reports-30k-blocks/Arangodb-16threads-summary.json",
    32: "reports-30k-blocks/Arangodb-32threads-summary.json",
    64: "reports-30k-blocks/Arangodb-64threads-summary.json",
}
mapping_report_30k_blocks_stress_batch = {
    100: "reports-30k-blocks/report-batch100-10000000-10030000-summary.json",
    500: "reports-30k-blocks/report-batch500-10000000-10030000-summary.json",
    1000: "reports-30k-blocks/report-batch1000-10000000-10030000-summary.json",
    2000: "reports-30k-blocks/report-batch2000-10000000-10030000-summary.json",
    5000: "reports-30k-blocks/report-batch5000-10000000-10030000-summary.json",
}

mapping_report_30k_blocks_optimize_stress_batch = {
    100: "reports-30k-blocks-optimize/report-batch100-10000000-10030000-summary.json",
    500: "reports-30k-blocks-optimize/report-batch500-10000000-10030000-summary.json",
    1000: "reports-30k-blocks-optimize/report-batch1000-10000000-10030000-summary.json",
    2000: "reports-30k-blocks-optimize/report-batch2000-10000000-10030000-summary.json",
    5000: "reports-30k-blocks-optimize/report-batch5000-10000000-10030000-summary.json",
}
mapping_report_30k_blocks_optimize_stress_threads = {
    4: "reports-30k-block-optimize-v2/Arangodb-4threads-block-10000000-10030000-summary.json",
    8: "reports-30k-block-optimize-v2/Arangodb-8threads-block-10000000-10030000-summary.json",
    16: "reports-30k-block-optimize-v2/Arangodb-16threads-block-10000000-10030000-summary.json",
    32: "reports-30k-block-optimize-v2/Arangodb-32threads-block-10000000-10030000-summary.json",
    64: "reports-30k-block-optimize-v2/Arangodb-64threads-block-10000000-10030000-summary.json",
}

stress_multi_threads = object_mapping_to_time(mapping_report_30k_blocks_stress_thread)
stress_batch_time = object_mapping_to_time(mapping_report_30k_blocks_stress_batch)
stress_batch_optimize_time = object_mapping_to_time(mapping_report_30k_blocks_optimize_stress_batch)
stress_thread_optimize_time = object_mapping_to_time(mapping_report_30k_blocks_optimize_stress_threads)

keys, read_times, write_times = object_report_to_lists(stress_thread_optimize_time)

avg_reads = []
avg_writes = []
for index, k in enumerate(keys):
    avg_reads.append(read_times[index] / k)
    avg_writes.append(write_times[index] / k)

x1 = keys
y11 = write_times
y12 = read_times
y13 = avg_reads
y14 = avg_writes
# plotting the line 1 points
# plt.plot(x1, y11, label="read")
# plt.plot(x1, y12, label="write")
plt.plot(x1, y13, label="avg read", marker="o")
plt.plot(x1, y14, label="avg write", marker="o")
# line 2 points

# keys, read_times, write_times = object_report_to_lists(stress_batch_optimize_time)
# x2 = keys
# y21 = read_times
# y22 = write_times
# # plotting the line 2 points
# plt.plot(x2, y21, label="read with index")
# plt.plot(x2, y22, label="write 2")
plt.xlabel('Thread number')

plt.ylabel('Execute time (s)')
# Set a title of the current axes.
# plt.title('Measure execute time of transactions')
# show a legend on the plot
plt.legend()
# Display a figure.
# plt.savefig("transaction-execute-time-tight.pdf", bbox_inches='tight')
plt.show()
