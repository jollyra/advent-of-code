from util import *


class Attack:
    def __init__(self, damage, attack_type):
        self.damage = damage
        self.attack_type = attack_type


class Group:
    def __init__(self, name, units, hp, immunities, weaknesses, attack, initiative):
        self.name = name
        self.units = units
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.army = None

    def __str__(self):
        return f'{self.name} contains {self.units}'

    def effective_power(self):
        return self.units * self.attack.damage

    def select_target(self, enemy_groups):
        if not len(enemy_groups):
            return None
        if not any(self.calc_damage(dg) for dg in enemy_groups):
            return None
        return sorted(enemy_groups, key=self._target_selection_sort_key)[0]

    def _target_selection_sort_key(self, defending_group):
        return -self.calc_damage(defending_group), -defending_group.effective_power(), -defending_group.initiative

    def calc_damage(self, defending_group):
        if self.attack.attack_type in defending_group.immunities:
            return 0
        if self.attack.attack_type in defending_group.weaknesses:
            return self.effective_power() * 2
        return self.effective_power()


class Army:
    def __init__(self, name):
        self.name = name
        self.groups = {}

    def __str__(self):
        s = f'{self.name}:\n'
        units = 0
        for key in self.groups:
            group = self.groups[key]
            s += f'{group}\n'
            units += group.units
        s += f'total units: {units}\n'
        return s

    def add(self, group):
        self.groups[group.name] = group
        group.army = self.name


class BattleField:
    def __init__(self, immune_system_army, infection_army):
        self.immune_system_army = immune_system_army
        self.infection_army = infection_army

    def all_groups(self):
        groups = []
        for army in [self.immune_system_army, self.infection_army]:
            for key in army.groups:
                groups.append(army.groups[key])
        return groups

    def clear_the_dead(self):
        for army in [self.immune_system_army, self.infection_army]:
            keys_to_delete = []
            for k, v in army.groups.items():
                if v.units <= 0:
                    keys_to_delete.append(k)

            for k in keys_to_delete:
                del army.groups[k]


def attack_order_sort_key(group):
    return -group.effective_power(), -group.initiative


def decreasing_initiative_key(target_selection):
    attacking_group = target_selection[0] 
    return -attacking_group.initiative


def get_enemy_groups(group, groups):
    return [g for g in groups if g.army != group.army]


def fight(ag, dg):
    dmg = ag.calc_damage(dg)
    casualties = dmg // dg.hp
    if casualties > dg.units:
        casualties = dg.units
    dg.units = dg.units - casualties
    print(f'{ag.army} {ag.name} attacks {dg.army} {dg.name}, killing {casualties} units')


def battle(battle_field):
    while len(battle_field.immune_system_army.groups) != 0 and len(battle_field.infection_army.groups) != 0:
        print('-------------------------------------------------------------------')
        ordered_groups = sorted(battle_field.all_groups(), key=attack_order_sort_key)
        targeted_groups = []
        target_selections = []
        for attacking_group in ordered_groups:
            enemy_groups = get_enemy_groups(attacking_group, battle_field.all_groups())
            remaining_enemy_groups = [g for g in enemy_groups if g not in targeted_groups]
            defending_group = attacking_group.select_target(remaining_enemy_groups)
            if defending_group:
                targeted_groups.append(defending_group)
                ag, dg = (attacking_group, defending_group)
                # print(f'{ag.army} {ag.name} would deal {dg.army} {dg.name} {ag.calc_damage(dg)} damage')
                target_selections.append((attacking_group, defending_group))

        target_selections_ordered = sorted(target_selections, key=decreasing_initiative_key)
        for selection in target_selections_ordered:
            fight(*selection)

        battle_field.clear_the_dead()

    print('\n-------------------------------------------------------------------')
    print('Battle finished!\n')
    print(battle_field.immune_system_army)
    print(battle_field.infection_army)


def run_test_battle():
    immune_system_army = Army('Immune System')
    immune_system_army.add(Group('Group 1', 17, 5390, [], ['radiation', 'bludgeoning'], Attack(4507, 'fire'), 2))
    immune_system_army.add(Group('Group 2', 989, 1274, ['fire'], ['bludgeoning', 'slashing'], Attack(25, 'slashing'), 3))
    print(immune_system_army)
    infection_army = Army('Infection')
    infection_army.add(Group('Group 1', 801, 4706, [], ['radiation'], Attack(116, 'bludgeoning'), 1))
    infection_army.add(Group('Group 2', 4485, 2961, ['radiation'], ['fire', 'cold'], Attack(12, 'slashing'), 4))
    print(infection_army)

    battle_field = BattleField(immune_system_army, infection_army)
    battle(battle_field)

def run_my_battle():
    # def __init__(self, name, units, hp, immunities, weaknesses, attack, initiative):
    immune_system_army = Army('Immune System')
    immune_system_army.add(Group('Group 1', 273, 8289, ['radiation', 'slashing'], ['bludgeoning'], Attack(261, 'cold damage'), 2))
    immune_system_army.add(Group('Group 2', 2016, 10188, ['cold', 'bludgeoning'], ['slashing', 'radiation'],  Attack(47, 'bludgeoning'), 14))
    immune_system_army.add(Group('Group 3', 3638, 9600, [], ['fire', 'cold'],  Attack(26, 'radiation'), 18))
    immune_system_army.add(Group('Group 4', 4154, 3839, [], [],  Attack(9, 'slashing'), 7))
    immune_system_army.add(Group('Group 5', 2872, 4441, ['radiation'], ['slashing'],  Attack(14, 'cold'), 15))
    immune_system_army.add(Group('Group 6', 906, 10657, ['fire'], [], Attack(105, 'fire'), 16))
    immune_system_army.add(Group('Group 7', 4497, 8474, ['slashing', 'radiation'], ['cold'],  Attack(18, 'slashing'), 1))
    immune_system_army.add(Group('Group 8', 2246, 6792, [], ['bludgeoning'], Attack(27, 'cold'), 17))
    immune_system_army.add(Group('Group 9', 3246, 1380, ['cold'], ['radiation'], Attack(4, 'cold'), 5))
    immune_system_army.add(Group('Group 10', 5042, 10450, [],[], Attack(18, 'fire'), 11))

    infection_army = Army('Infection')
    infection_army.add(Group('Group 1', 982, 23562, [], [],  Attack(47, 'radiation'), 6))
    infection_army.add(Group('Group 2', 601, 44172, ['radiation'], [], Attack(120, 'fire'), 12))
    infection_army.add(Group('Group 3', 6035, 9260, ['slashing'], ['fire'], Attack(2, 'fire'), 4))
    infection_army.add(Group('Group 4', 476, 34584, [], ['slashing', 'fire'],  Attack(130, 'slashing'), 3))
    infection_army.add(Group('Group 5', 6608, 46197, [], [],  Attack(13, 'fire'), 8))
    infection_army.add(Group('Group 6', 275, 37639, ['cold', 'fire'], [],  Attack(250, 'radiation'), 9))
    infection_army.add(Group('Group 7', 1428, 47260, [], ['slashing'], Attack(64, 'bludgeoning'), 19))
    infection_army.add(Group('Group 8', 8479, 23902, [], ['slashing', 'fire'], Attack(4, 'bludgeoning'), 13))
    infection_army.add(Group('Group 9', 2620, 11576, [], ['radiation', 'bludgeoning'], Attack(7, 'radiation'), 10))
    infection_army.add(Group('Group 10', 2107, 30838, [], ['radiation', 'fire'],  Attack(28, 'cold'), 20))

    battle_field = BattleField(immune_system_army, infection_army)
    battle(battle_field)

def main():
    run_test_battle()
    run_my_battle()


if __name__ == '__main__':
    main()
