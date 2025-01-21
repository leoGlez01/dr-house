-- Crear roles para los diferentes tipos de usuarios
CREATE ROLE patient_role;
CREATE ROLE doctor_role;
CREATE ROLE admin_role;

-- Asignar permisos para pacientes
GRANT SELECT, INSERT, UPDATE ON users TO patient_role;
GRANT SELECT, INSERT, UPDATE ON appointments, medical_records TO patient_role;

-- Asignar permisos para médicos
GRANT SELECT, INSERT, UPDATE ON users TO doctor_role;
GRANT SELECT, INSERT, UPDATE ON appointments, medical_records, treatments, prescriptions TO doctor_role;
GRANT SELECT, INSERT, UPDATE ON medications TO doctor_role;

-- Asignar permisos para administradores
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin_role;