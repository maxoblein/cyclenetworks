function [cycleProportionFlowWeighted,effectiveLengthFlowWeighted]=...
    computeMetrics(ODmatrix,flowPath,edgePath,isEdgeCycle,lengthEdge,omega)

cycleProportionFlowWeighted = 0;
effectiveLengthFlowWeighted = 0;
%
for i=1:size(ODmatrix,1)     % loop over O
    for j=1:size(ODmatrix,2) % loop over D
        for k=1:length(flowPath{i,j})
            % weight at this point is flowPath{i,j}(k)
            % but what are the properties of this path?
            path=edgePath{i,j}{k};  % edges in the path in question
            roadEdge = path(~isEdgeCycle(path));
            cycleEdge = path(isEdgeCycle(path));
            roadLength = sum(lengthEdge(roadEdge));
            cycleLength = sum(lengthEdge(cycleEdge));
            cycleProportion = cycleLength/(cycleLength+roadLength);
            effectiveLength = cycleLength + omega*roadLength;
            cycleProportionFlowWeighted = cycleProportionFlowWeighted + cycleProportion*flowPath{i,j}(k);
            effectiveLengthFlowWeighted = effectiveLengthFlowWeighted + effectiveLength*flowPath{i,j}(k);
        end
    end
end
end