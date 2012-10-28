import clusters


blognames, words, data = clusters.readfile('blogdata.txt')

print '--------------------'
print 'hierarchical clustering'
print '--------------------'

clust = clusters.hcluster(data)
clusters.printclust(clust, labels=blognames)


print '--------------------'
print 'k-Means clustering'
print '--------------------'

numclusters = 3
clust = clusters.kcluster(data, k=numclusters)
for i in range(numclusters):
    print 'cluster[%d]:' % i
    currentcluster = clust[i]
    for r in currentcluster:
        print '\t%s' % blognames[r]
    print
