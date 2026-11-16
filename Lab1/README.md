# Lab 1: Requirements Engineering & UML Use-Case Modelling

**Problem Statement #18 — Healthcare & Telemedicine**
**Clinical Trial Subject Recruitment Engine**

## Overview
An eligibility pre-screening platform for clinical trials, tracking subject inclusion/exclusion criteria, informed consent milestones, and visit compliance logs.

**Stakeholders / Actors:** Trial Candidate, Clinical Researcher, System Administrator

## Deliverables

| File | Description |
|---|---|
| [`Requirements_Table.docx`](./Requirements_Table.docx) | 5 Functional Requirements (FR-001–FR-005) and 2 Non-Functional Requirements (NFR-001–NFR-002), with ID, Type, Description, Priority, Acceptance Criteria, and Rationale |
| [`UML_Use_Case_Diagram.pdf`](./UML_Use_Case_Diagram.pdf) | Use-case diagram showing all actors, 7 use cases, one «include» relationship, and one «extend» relationship |
| [`Use_Case_Flow.docx`](./Use_Case_Flow.docx) | One-page flow specification for UC-02: Check Eligibility, with Preconditions, Postconditions, Main Success Scenario, and an Alternate Flow |

## Actors
- **Trial Candidate** — applies to join the trial, completes the survey, signs consent, attends visits.
- **Clinical Researcher** — reviews eligibility, monitors visit compliance, receives alerts.
- **System Administrator** — configures trial protocols and manages accounts.

## Use Cases
- UC-01 Submit Eligibility Survey
- UC-02 Check Eligibility *(includes UC-01)*
- UC-03 Sign Informed Consent
- UC-04 View Candidate List
- UC-05 Log Visit Compliance
- UC-06 Notify Missed Visit *(extends UC-05)*
- UC-07 Manage Trial Protocol
