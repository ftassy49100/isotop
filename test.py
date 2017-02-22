# coding: utf8
from app import db
from app.models.qualityFolder import QualityFolder
from app.models.anomalyType import AnomalyType

qf = QualityFolder()
at = AnomalyType.query.get(2)
print(at)
at.quality_folders.append(qf)
print (at.quality_folders)
