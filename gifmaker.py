import imageio

filenames = ['lpic_figs/batches_2000_100_20/batch_1.png','lpic_figs/batches_2000_100_20/batch_2.png','lpic_figs/batches_2000_100_20/batch_3.png','lpic_figs/batches_2000_100_20/batch_4.png','lpic_figs/batches_2000_100_20/batch_5.png','lpic_figs/batches_2000_100_20/batch_6.png','lpic_figs/batches_2000_100_20/batch_7.png','lpic_figs/batches_2000_100_20/batch_8.png','lpic_figs/batches_2000_100_20/batch_9.png','lpic_figs/batches_2000_100_20/batch_10.png','lpic_figs/batches_2000_100_20/batch_11.png','lpic_figs/batches_2000_100_20/batch_12.png','lpic_figs/batches_2000_100_20/batch_13.png','lpic_figs/batches_2000_100_20/batch_14.png','lpic_figs/batches_2000_100_20/batch_15.png','lpic_figs/batches_2000_100_20/batch_16.png','lpic_figs/batches_2000_100_20/batch_17.png','lpic_figs/batches_2000_100_20/batch_18.png','lpic_figs/batches_2000_100_20/batch_19.png','lpic_figs/batches_2000_100_20/batch_20.png']


images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('batches_2000_100_20.gif', images)
