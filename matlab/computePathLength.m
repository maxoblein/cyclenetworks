function lengthPath = computePathLength(edgePath,isEdgeCycle,lengthEdge,omega)
% function lengthPath = computePathLength(edgePath,isEdgeCycle,lengthEdge,omega)
% omega is set as the multiple that roads appear to be - is this right?
for i=1:size(edgePath,1)
    for j=1:size(edgePath,2)
        listPath=edgePath{i,j};
        tmpLength=[];
        for k=1:length(listPath)
            tmp=listPath{k};
            tmpLength(k)=sum(lengthEdge(tmp).*(1+(omega-1)*~isEdgeCycle(tmp)));
            % this needs checking - partic how I do omega
        end
        lengthPath{i,j}=tmpLength;
    end
end


end

