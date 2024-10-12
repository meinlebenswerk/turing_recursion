from typing import Literal


class TuringMachine:
    def __init__(
        self,
        tape: list[int | str],
        blank_symbol: int | str | None,
        initial_state: str,
        final_states: set[str],
        transition_function: dict[tuple[str, int | str], tuple[int | str, Literal['R', 'L'], str]],
        boundary_condition: Literal['fixed', 'wrapping'] = 'fixed',
    ):
        self.tape = list(tape)
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.boundary_condition = boundary_condition

    def _print_tape(self, with_index: bool = False):
        tape_len = len(self.tape)
        print(f'\ttape:  [{", ".join([f'{cell}'.ljust(len(str(tape_len))) for cell in self.tape])}]')
        if with_index:
            print(f'\tindex: [{", ".join([f'{i}'.ljust(len(str(tape_len))) for i in range(tape_len)])}]')

    def step(self, debug: bool = False):
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) in self.transition_function:
            new_symbol, direction, new_state = self.transition_function[(self.current_state, current_symbol)]
            if debug:
                print(f"{self.head_position} -> {self.head_position + (1 if direction == 'R' else -1)} | state: {self.current_state} -> {new_state}, symbol: {current_symbol} -> {new_symbol} | dir: {direction}")
                # print(f"\ttape: {self.tape}")
                self._print_tape()
            self.tape[self.head_position] = new_symbol
            if debug:
                # print(f"\ttape: {self.tape}")
                self._print_tape(with_index=True)
            self.head_position += 1 if direction == 'R' else -1
            if self.boundary_condition == 'fixed':
                if self.head_position < 0 or self.head_position >= len(self.tape):
                    raise Exception(f"Head position out of bounds: {self.head_position}")
            elif self.boundary_condition == 'wrapping':
                self.head_position %= len(self.tape)
            else:
                raise Exception(f"Unknown boundary condition: {self.boundary_condition}")

            self.current_state = new_state
        else:
            raise Exception(f"No transition defined for this state ({self.current_state}) and symbol ({current_symbol})")

    def run(self, debug: bool = False, max_steps: int | None = None) -> int:
        num_steps = 0
        self.step(debug) # do ... while (so we can interrupt at the right time)
        while self.current_state not in self.final_states:
            self.step(debug)
            num_steps += 1
            if max_steps is not None and num_steps >= max_steps:
                break
        return num_steps