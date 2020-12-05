-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT
	SUM((C.score) * P.weight) / (SUM(P.weight)) 'avg'
	FROM corrections AS C
	INNER JOIN projects AS P
	ON P.id = C.project_id
	WHERE C.user_id = user_id)
	WHERE users.id = user_id);
END $$
DELIMITER ;
