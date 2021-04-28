%loop scipt to get distributions of scores for one and two batches%

N = 100;

scores = ones(2,N);

for i = 1:N
    
   scores{i} = MaxIdeas();
    
end

scores