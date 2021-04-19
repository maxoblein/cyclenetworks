function [flowEdge,flowPath] = allocateTraffic(ODmatrix,lengthPath,lambda,numEdge,edgePath)
% function [flowEdge,flowPath] = allocateTraffic(ODmatrix,lengthPath,lambda,numEdge,edgePath)
% compute path flows first
for i=1:size(ODmatrix,1)     % loop over O
    for j=1:size(ODmatrix,2) % loop over D
        tmp=lengthPath{i,j};
        flowPath{i,j}=zeros(length(tmp),1);
        if isfinite(lambda)
            flowPath{i,j}=(exp(-lambda*tmp)/sum(exp(-lambda*tmp)))*ODmatrix(i,j);
        else
            [~,ind]=min(lengthPath{i,j});
            flowPath{i,j}(ind)=ODmatrix(i,j);
        end
    end
end
% load path flows onto edges.
flowEdge=zeros(numEdge,1);
for i=1:size(ODmatrix,1)
    for j=1:size(ODmatrix,2)
        for k=1:length(flowPath{i,j})
            flowEdge(edgePath{i,j}{k})=flowEdge(edgePath{i,j}{k})+...
                flowPath{i,j}(k);
        end
    end
end
end
% I believe this might work...