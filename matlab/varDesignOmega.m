%vary design omega
omegaTest = linspace(1,10,100)
for i = 1:length(omegaTest)
[pODoneBatch(i),pODtwoBatch(i),effectiveLenOneBatch(i),effectiveLenTwoBatch(i)] = Ensemble(omegaTest(i),2);
end



scatter(omegaTest,effectiveLenTwoBatch,300,'.')


