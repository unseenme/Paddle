from dataclasses import dataclass

@dataclass
class InstructionId
    instruction_id: int

    def __hash__(self):
        return hash(self.instruction_id)

    @classmethod
    def GetDAGGenClassToDerivedClassMap(cls):
        return InstructionId


def MakeUniqueInstructionId():
    return InstructionId(
        instruction_id=GetUniqueInstructionId()
    )

def GetUniqueInstructionId():
    global global_instruction_id_seq_no
    global_instruction_id_seq_no += 1
    return global_instruction_id_seq_no

global_instruction_id_seq_no = 0